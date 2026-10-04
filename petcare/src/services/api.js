// Actualiza la constante con tu servidor local de Django
const BASE_URL = 'http://127.0.0.1:8000/api/reservas/';

// IMPORTANTE: Asegúrate de pegar TU token real aquí, manteniendo la palabra "Token" y el espacio
const TOKEN = 'Token PEGA_AQUI_TU_TOKEN_DE_THUNDER_CLIENT';

export async function getReservasAPI() {
  const res = await fetch(BASE_URL, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': TOKEN
    }
  });
  if (!res.ok) throw new Error('Error al obtener reservas');
  const data = await res.json();
  // El GET no cambió, sigue devolviendo {"datos": [...]}
  return data.datos; 
}

export async function createReservaAPI(reserva) {
  const res = await fetch(BASE_URL, {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': TOKEN
    },
    body: JSON.stringify(reserva),
  });
  if (!res.ok) throw new Error('Error al crear reserva');
  
  // Procesamos la nueva estructura (Mensaje + Datos)
  const respuesta = await res.json();
  console.log("Aviso de Django (POST):", respuesta.mensaje);
  
  return respuesta.datos; // Extraemos la llave "datos" para que React funcione
}

export async function updateReservaAPI(id, datosActualizados) {
  const res = await fetch(`${BASE_URL}${id}/`, {
    method: 'PUT',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': TOKEN
    },
    body: JSON.stringify(datosActualizados),
  });
  if (!res.ok) throw new Error('Error al actualizar reserva');
  
  // Procesamos la nueva estructura (Mensaje + Datos)
  const respuesta = await res.json();
  console.log("Aviso de Django (PUT):", respuesta.mensaje);
  
  return respuesta.datos; // Extraemos la llave "datos" para que React funcione
}

export async function deleteReservaAPI(id) {
  const res = await fetch(`${BASE_URL}${id}/`, {
    method: 'DELETE',
    headers: { 
      'Authorization': TOKEN
    }
  });
  if (!res.ok) throw new Error('Error al eliminar reserva');
  
  // Procesamos el mensaje personalizado que ahora envía el backend
  const respuesta = await res.json();
  console.log("Aviso de Django (DELETE):", respuesta.mensaje);
  
  return true; 
}

// Función simulada para que el componente Newsletter de la página web no se rompa
export async function apiSubscribe(email) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ status: 200, message: "Suscripción exitosa" });
    }, 1000);
  });
}