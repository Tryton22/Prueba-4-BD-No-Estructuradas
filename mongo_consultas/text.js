db.encuestas.insertOne({
  usuario: "Jorge Toro",
  fecha_encuesta: "2025-07-08",
  preguntas: [
    { pregunta: "¿Quedó conforme con la atención?", respuesta: "Sí" },
    { pregunta: "¿El tiempo de respuesta fue adecuado?", respuesta: "Sí" }
  ]
})

db.comentarios.insertOne({
  usuario: "Pedro Muñoz",
  fecha: "2025-07-08",
  comentario: "Muy buena atención al cliente, solucionaron rápido el problema.",
  adjuntos: [
    { nombre_archivo: "boleta_servicio.pdf", url: "/uploads/boleta_servicio.pdf" }
  ]
})

db.analisis_sentimiento.insertOne({
  usuario: "@cliente_789",
  origen: "facebook",
  fecha: "2025-07-08",
  comentario: "Excelente servicio, todo rápido y claro.",
  sentimiento: "positivo",
  score: 0.95
})

//ENCUESTAS
({
  "_id": ObjectId,
  "usuario": "String",
  "fecha_encuesta": "String (YYYY-MM-DD)",
  "preguntas": [
    { "pregunta": "String", "respuesta": "String" }
  ],
  "puntaje_total": Float
})


//COMENTARIOS
({
  "_id": ObjectId,
  "usuario": "String",
  "fecha": "String (YYYY-MM-DD)",
  "comentario": "String",
  "adjuntos": [
    { "nombre_archivo": "String", "url": "String" }
  ]
})

//ANALISIS SENTIMIENTOS
({
  "_id": ObjectId,
  "usuario": "String",
  "origen": "String (por ejemplo: 'twitter', 'facebook')",
  "fecha": "String (YYYY-MM-DD)",
  "comentario": "String",
  "sentimiento": "String",
  "score": Float
})

