import React, { useState, useEffect } from 'react';
import { getReservasAPI, createReservaAPI, updateReservaAPI, deleteReservaAPI } from '../services/api';

const CrudMascotas = () => {
  const [reservas, setReservas] = useState([]);
  const [loading, setLoading] = useState(true);
  
  // Estado plano para controlar los campos del formulario de forma sencilla
  const [formData, setFormData] = useState({
    id: '',
    dueñoNombre: '',
    dueñoTelefono: '',
    mascotaNombre: '',
    mascotaTipo: '',
    mascotaRaza: '',
    servicioNombre: '',
    fecha: '',
    hora: '',
    estado: 'pendiente'
  });
  
  const [isEditing, setIsEditing] = useState(false);

  // Función para cargar los registros desde el servidor central
  const cargarReservas = async () => {
    setLoading(true);
    const datosAPI = await getReservasAPI();
    setReservas(datosAPI);
    setLoading(false);
  };

  useEffect(() => {
    cargarReservas();
  }, []);

  // Manejador de cambios en los inputs del formulario
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Procesar envío del formulario (Crear o Editar)
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Construcción del modelo de datos EXACTO requerido por la API centralizada
    const modeloDeDatosAPI = {
      dueño: {
        nombre: formData.dueñoNombre,
        telefono: formData.dueñoTelefono
      },
      mascota: {
        nombre: formData.mascotaNombre,
        tipo: formData.mascotaTipo,
        raza: formData.mascotaRaza
      },
      servicioNombre: formData.servicioNombre,
      fecha: formData.fecha,
      hora: formData.hora,
      estado: formData.estado
    };

    try {
      if (isEditing) {
        // Petición de actualización
        await updateReservaAPI(formData.id, modeloDeDatosAPI);
        setIsEditing(false);
      } else {
        // Petición de creación
        const respuesta = await createReservaAPI(modeloDeDatosAPI);
        if (!respuesta) return; // Si la API rechazó la creación, detenemos el proceso
      }

      // Limpiar campos y esperar obligatoriamente la recarga de datos del servidor
      limpiarFormulario();
      await cargarReservas(); 
    } catch (error) {
      console.error("Error al procesar el formulario:", error);
    }
  };

  // Mapear el objeto anidado de la API al estado plano del formulario para editar
  const handleEdit = (reserva) => {
    setFormData({
      id: reserva._id,
      dueñoNombre: reserva.dueño?.nombre || '',
      dueñoTelefono: reserva.dueño?.telefono || '',
      mascotaNombre: reserva.mascota?.nombre || '',
      mascotaTipo: reserva.mascota?.tipo || '',
      mascotaRaza: reserva.mascota?.raza || '',
      servicioNombre: reserva.servicioNombre || '',
      fecha: reserva.fecha || '',
      hora: reserva.hora || '',
      estado: reserva.estado || 'pendiente'
    });
    setIsEditing(true);
  };

  // Eliminar un registro mediante confirmación nativa
  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro de eliminar esta reserva médica de la base de datos central?')) {
      await deleteReservaAPI(id);
      await cargarReservas(); 
    }
  };

  // Restablecer el formulario a su estado vacío original
  const limpiarFormulario = () => {
    setFormData({
      id: '',
      dueñoNombre: '',
      dueñoTelefono: '',
      mascotaNombre: '',
      mascotaTipo: '',
      mascotaRaza: '',
      servicioNombre: '',
      fecha: '',
      hora: '',
      estado: 'pendiente'
    });
    setIsEditing(false);
  };

  return (
    <div className="container py-5 mt-4">
      <h2 className="fw-bold mb-2 text-center text-primary">Control de Reservas Médicas</h2>
      <p className="text-center text-muted mb-5">Modelo de datos centralizado y sincronizado con la API</p>
      
      <div className="row">
        {/* Sección del Formulario */}
        <div className="col-lg-4 mb-4">
          <div className="card shadow-sm border-0">
            <div className={`card-header text-white ${isEditing ? 'bg-success' : 'bg-primary'}`}>
              <h5 className="mb-0">{isEditing ? '✏️ Editar Reserva' : '➕ Nueva Reserva'}</h5>
            </div>
            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <h6 className="text-secondary fw-bold border-bottom pb-1 mb-3">Datos del Dueño</h6>
                <div className="mb-2">
                  <label className="form-label small mb-1">Nombre Completo</label>
                  <input type="text" className="form-control form-control-sm" name="dueñoNombre" value={formData.dueñoNombre} onChange={handleChange} required />
                </div>
                <div className="mb-3">
                  <label className="form-label small mb-1">Teléfono</label>
                  <input type="text" className="form-control form-control-sm" name="dueñoTelefono" placeholder="+56 9..." value={formData.dueñoTelefono} onChange={handleChange} required />
                </div>

                <h6 className="text-secondary fw-bold border-bottom pb-1 mb-3">Datos de la Mascota</h6>
                <div className="mb-2">
                  <label className="form-label small mb-1">Nombre Mascota</label>
                  <input type="text" className="form-control form-control-sm" name="mascotaNombre" value={formData.mascotaNombre} onChange={handleChange} required />
                </div>
                <div className="row g-2 mb-2">
                  <div className="col-6">
                    <label className="form-label small mb-1">Tipo</label>
                    <select className="form-select form-select-sm" name="mascotaTipo" value={formData.mascotaTipo} onChange={handleChange} required>
                      <option value="">Seleccione...</option>
                      <option value="perro">Perro</option>
                      <option value="gato">Gato</option>
                      <option value="ave">Ave</option>
                      <option value="otro">Otro</option>
                    </select>
                  </div>
                  <div className="col-6">
                    <label className="form-label small mb-1">Raza</label>
                    <input type="text" className="form-control form-control-sm" name="mascotaRaza" value={formData.mascotaRaza} onChange={handleChange} required />
                  </div>
                </div>

                <h6 className="text-secondary fw-bold border-bottom pb-1 mb-3">Detalles del Servicio</h6>
                <div className="mb-2">
                  <label className="form-label small mb-1">Servicio</label>
                  <input type="text" className="form-control form-control-sm" name="servicioNombre" placeholder="Ej: Vacuna, Castración" value={formData.servicioNombre} onChange={handleChange} required />
                </div>
                <div className="row g-2 mb-3">
                  <div className="col-6">
                    <label className="form-label small mb-1">Fecha</label>
                    <input type="date" className="form-control form-control-sm" name="fecha" value={formData.fecha} onChange={handleChange} required />
                  </div>
                  <div className="col-6">
                    <label className="form-label small mb-1">Hora</label>
                    <input type="time" className="form-control form-control-sm" name="hora" value={formData.hora} onChange={handleChange} required />
                  </div>
                </div>
                <div className="mb-4">
                  <label className="form-label small mb-1">Estado de Reserva</label>
                  <select className="form-select form-select-sm" name="estado" value={formData.estado} onChange={handleChange}>
                    <option value="pendiente">Pendiente</option>
                    <option value="confirmada">Confirmada</option>
                  </select>
                </div>

                <div className="d-grid gap-2">
                  <button type="submit" className={`btn btn-sm text-white ${isEditing ? 'btn-success' : 'btn-primary'}`}>
                    {isEditing ? 'Guardar Cambios' : 'Registrar en API'}
                  </button>
                  {isEditing && (
                    <button type="button" className="btn btn-sm btn-secondary" onClick={limpiarFormulario}>
                      Cancelar
                    </button>
                  )}
                </div>
              </form>
            </div>
          </div>
        </div>

        {/* Tabla de Visualización de Datos de la API */}
        <div className="col-lg-8">
          <div className="card shadow-sm border-0">
            <div className="card-body">
              <div className="d-flex justify-content-between align-items-center mb-3">
                <h5 className="card-title mb-0 fw-bold">Reservas de la Red Colectiva</h5>
                <button className="btn btn-sm btn-outline-secondary" onClick={cargarReservas}>🔄 Refrescar</button>
              </div>
              
              {loading ? (
                <div className="text-center py-5">
                  <div className="spinner-border text-primary" role="status"></div>
                  <p className="mt-2 text-muted">Conectando con la API...</p>
                </div>
              ) : (
                <div className="table-responsive">
                  <table className="table table-hover align-middle small">
                    <thead className="table-light">
                      <tr>
                        <th>Mascota</th>
                        <th>Dueño</th>
                        <th>Servicio</th>
                        <th>Fecha / Hora</th>
                        <th>Estado</th>
                        <th className="text-end">Acciones</th>
                      </tr>
                    </thead>
                    <tbody>
                      {reservas.length === 0 ? (
                        <tr>
                          <td colSpan="6" className="text-center text-muted py-4">No hay registros en el servidor central.</td>
                        </tr>
                      ) : (
                        reservas.map((item) => (
                          <tr key={item._id}>
                            <td>
                              <span className="fw-bold text-capitalize">{item.mascota?.nombre || 'Sin nombre'}</span>
                              <br />
                              <small className="text-muted text-uppercase">{item.mascota?.tipo || 'Desconocido'} ({item.mascota?.raza || 'N/A'})</small>
                            </td>
                            <td>
                              <span className="text-capitalize">{item.dueño?.nombre || 'Anónimo'}</span>
                              <br />
                              <small className="text-muted">{item.dueño?.telefono || 'Sin Teléfono'}</small>
                            </td>
                            <td>
                              <span className="badge bg-light text-dark border">{item.servicioNombre || 'Control General'}</span>
                            </td>
                            <td>
                              {item.fecha || 'Sin fecha'}
                              <br />
                              <small className="text-muted">{item.hora || '--:--'}</small>
                            </td>
                            <td>
                              <span className={`badge rounded-pill ${item.estado === 'confirmada' ? 'bg-success-subtle text-success' : 'bg-warning-subtle text-warning'}`}>
                                {item.estado || 'pendiente'}
                              </span>
                            </td>
                            <td className="text-end">
                              <button className="btn btn-xs btn-outline-primary me-1" onClick={() => handleEdit(item)} title="Editar">
                                ✏️
                              </button>
                              <button className="btn btn-xs btn-outline-danger" onClick={() => handleDelete(item._id)} title="Eliminar">
                                🗑️
                              </button>
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CrudMascotas;