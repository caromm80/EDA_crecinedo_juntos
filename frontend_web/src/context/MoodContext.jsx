import React, { createContext, useContext, useState, useEffect } from 'react';

const MoodContext = createContext();

// 22 registros iniciales realistas precargados para asegurar visualizaciones y estadísticas completas de inmediato
const ENTRADAS_INICIALES = [
  {
    id: 1,
    fecha: '2026-11-03',
    usuario: 'Carolina Morales',
    nivel_animo: 5,
    emocion: 'Radiante',
    categoria: 'Crecimiento Personal',
    motivo_gratitud: 'Por culminar con éxito la arquitectura de nuestra app con mi equipo de trabajo.',
    horas_sueno: 8.0,
    energia_pct: 95
  },
  {
    id: 2,
    fecha: '2026-11-02',
    usuario: 'Carolina Morales',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Bienestar',
    motivo_gratitud: 'Por una tarde tranquila disfrutando de un té caliente y una buena lectura.',
    horas_sueno: 7.5,
    energia_pct: 85
  },
  {
    id: 3,
    fecha: '2026-11-01',
    usuario: 'Carolina Morales',
    nivel_animo: 4,
    emocion: 'Motivado',
    categoria: 'Estudio',
    motivo_gratitud: 'Por aprender a estructurar componentes desacoplados en React y Context API.',
    horas_sueno: 7.0,
    energia_pct: 80
  },
  {
    id: 4,
    fecha: '2026-10-31',
    usuario: 'Carolina Morales',
    nivel_animo: 3,
    emocion: 'Estable',
    categoria: 'Relaciones',
    motivo_gratitud: 'Por las risas y la llamada sorpresa de mis primos en la noche de celebración.',
    horas_sueno: 6.5,
    energia_pct: 70
  },
  {
    id: 5,
    fecha: '2026-10-30',
    usuario: 'Carolina Morales',
    nivel_animo: 2,
    emocion: 'Pensativo',
    categoria: 'Autocuidado',
    motivo_gratitud: 'Por reconocer que necesito pausas activas cuando la carga académica sube.',
    horas_sueno: 5.5,
    energia_pct: 60
  },
  {
    id: 6,
    fecha: '2026-10-29',
    usuario: 'Carolina Morales',
    nivel_animo: 5,
    emocion: 'Radiante',
    categoria: 'Salud',
    motivo_gratitud: 'Por una caminata matutina en el parque con aire fresco y cielo despejado.',
    horas_sueno: 8.5,
    energia_pct: 90
  },
  {
    id: 7,
    fecha: '2026-10-28',
    usuario: 'Mateo Restrepo',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Familia',
    motivo_gratitud: 'Por el almuerzo casero preparado por mi mamá con tanto amor.',
    horas_sueno: 7.5,
    energia_pct: 85
  },
  {
    id: 8,
    fecha: '2026-10-27',
    usuario: 'Mateo Restrepo',
    nivel_animo: 5,
    emocion: 'Motivado',
    categoria: 'Trabajo',
    motivo_gratitud: 'Agradecido por solucionar un bug complejo en la base de datos sin frustración.',
    horas_sueno: 7.0,
    energia_pct: 90
  },
  {
    id: 9,
    fecha: '2026-10-26',
    usuario: 'Valentina Gómez',
    nivel_animo: 3,
    emocion: 'Estable',
    categoria: 'Bienestar',
    motivo_gratitud: 'Por tener un techo cómodo donde escuchar la lluvia caer en la noche.',
    horas_sueno: 6.8,
    energia_pct: 75
  },
  {
    id: 10,
    fecha: '2026-10-25',
    usuario: 'Valentina Gómez',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Amistad',
    motivo_gratitud: 'Por los amigos sinceros que te escuchan sin juzgar en momentos de cambio.',
    horas_sueno: 7.2,
    energia_pct: 80
  },
  {
    id: 11,
    fecha: '2026-10-24',
    usuario: 'Andrés Felipe',
    nivel_animo: 2,
    emocion: 'Apapacho',
    categoria: 'Autocuidado',
    motivo_gratitud: 'Por permitirme llorar un momento y saber que mañana será otro comienzo.',
    horas_sueno: 5.0,
    energia_pct: 55
  },
  {
    id: 12,
    fecha: '2026-10-23',
    usuario: 'Andrés Felipe',
    nivel_animo: 4,
    emocion: 'Motivado',
    categoria: 'Deporte',
    motivo_gratitud: 'Por retomar mi entrenamiento en bicicleta y sentir la energía del cuerpo.',
    horas_sueno: 7.8,
    energia_pct: 85
  },
  {
    id: 13,
    fecha: '2026-10-22',
    usuario: 'Sofía Ramírez',
    nivel_animo: 5,
    emocion: 'Radiante',
    categoria: 'Logro',
    motivo_gratitud: 'Por recibir retroalimentación positiva de los profesores en el proyecto integrador.',
    horas_sueno: 8.0,
    energia_pct: 95
  },
  {
    id: 14,
    fecha: '2026-10-21',
    usuario: 'Sofía Ramírez',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Naturaleza',
    motivo_gratitud: 'Por un atardecer precioso de tonos naranjas y violetas desde mi ventana.',
    horas_sueno: 7.2,
    energia_pct: 80
  },
  {
    id: 15,
    fecha: '2026-10-20',
    usuario: 'Santiago López',
    nivel_animo: 3,
    emocion: 'Estable',
    categoria: 'Creatividad',
    motivo_gratitud: 'Por volver a dibujar y reencontrarme con mi pasatiempo favorito.',
    horas_sueno: 6.8,
    energia_pct: 70
  },
  {
    id: 16,
    fecha: '2026-10-19',
    usuario: 'Camila Torres',
    nivel_animo: 5,
    emocion: 'Radiante',
    categoria: 'Familia',
    motivo_gratitud: 'Por la salud recuperada de mi abuela y tenerla cerquita para abrazarla.',
    horas_sueno: 8.2,
    energia_pct: 95
  },
  {
    id: 17,
    fecha: '2026-10-18',
    usuario: 'Daniel Castro',
    nivel_animo: 4,
    emocion: 'Motivado',
    categoria: 'Estudio',
    motivo_gratitud: 'Por comprender finalmente los algoritmos de ordenamiento y estructuras de datos.',
    horas_sueno: 7.4,
    energia_pct: 85
  },
  {
    id: 18,
    fecha: '2026-10-17',
    usuario: 'Mariana Vargas',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Paz Mental',
    motivo_gratitud: 'Por una sesión de respiración profunda que me ayudó a soltar el estrés.',
    horas_sueno: 7.5,
    energia_pct: 80
  },
  {
    id: 19,
    fecha: '2026-10-16',
    usuario: 'Sebastián Herrera',
    nivel_animo: 1,
    emocion: 'Apapacho',
    categoria: 'Autocuidado',
    motivo_gratitud: 'Por una taza de chocolate caliente y las palabras de consuelo de mi mejor amigo.',
    horas_sueno: 4.8,
    energia_pct: 45
  },
  {
    id: 20,
    fecha: '2026-10-15',
    usuario: 'Lucía Mendoza',
    nivel_animo: 5,
    emocion: 'Radiante',
    categoria: 'Espiritualidad',
    motivo_gratitud: 'Por sentirme en profunda gratitud y armonía con el momento presente.',
    horas_sueno: 8.0,
    energia_pct: 90
  },
  {
    id: 21,
    fecha: '2026-10-14',
    usuario: 'Alejandro Morales',
    nivel_animo: 4,
    emocion: 'Calmado',
    categoria: 'Trabajo',
    motivo_gratitud: 'Por haber completado las entregas a tiempo sin tener que trasnochar.',
    horas_sueno: 7.6,
    energia_pct: 85
  },
  {
    id: 22,
    fecha: '2026-10-13',
    usuario: 'Valeria Rojas',
    nivel_animo: 5,
    emocion: 'Motivado',
    categoria: 'Superación',
    motivo_gratitud: 'Por atreverme a presentar en público venciendo los nervios iniciales.',
    horas_sueno: 7.8,
    energia_pct: 90
  }
];

export const MoodProvider = ({ children }) => {
  const [entries, setEntries] = useState(() => {
    const saved = localStorage.getItem('lumi_gratitude_entries');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      } catch (err) {
        console.error("Error al cargar registros desde localStorage:", err);
      }
    }
    return ENTRADAS_INICIALES;
  });

  // Guardar en localStorage ante cualquier cambio de estado
  useEffect(() => {
    localStorage.setItem('lumi_gratitude_entries', JSON.stringify(entries));
  }, [entries]);

  // CREATE
  const addEntry = (newEntryData) => {
    const nuevaEntrada = {
      id: Date.now(),
      fecha: newEntryData.fecha || new Date().toISOString().split('T')[0],
      usuario: newEntryData.usuario || 'Carolina Morales',
      nivel_animo: Number(newEntryData.nivel_animo) || 3,
      emocion: newEntryData.emocion || 'Calmado',
      categoria: newEntryData.categoria || 'Bienestar',
      motivo_gratitud: newEntryData.motivo_gratitud || 'Agradecido por hoy.',
      horas_sueno: Number(newEntryData.horas_sueno) || 7.0,
      energia_pct: Number(newEntryData.energia_pct) || 80
    };

    setEntries(prev => [nuevaEntrada, ...prev]);
    return nuevaEntrada;
  };

  // UPDATE
  const updateEntry = (id, updatedFields) => {
    setEntries(prev =>
      prev.map(item => (item.id === Number(id) ? { ...item, ...updatedFields } : item))
    );
  };

  // DELETE
  const deleteEntry = (id) => {
    setEntries(prev => prev.filter(item => item.id !== Number(id)));
  };

  // READ SINGLE
  const getEntryById = (id) => {
    return entries.find(item => item.id === Number(id));
  };

  // MÉTRICAS Y ESTADÍSTICAS GLOBALES
  const getStats = () => {
    const total = entries.length;
    if (total === 0) {
      return {
        total: 0,
        promedioAnimo: 0,
        tasaPositiva: 0,
        rachaDias: 0,
        emocionFrecuente: 'Ninguna',
        distribucionEmociones: {}
      };
    }

    const sumaAnimo = entries.reduce((acc, curr) => acc + curr.nivel_animo, 0);
    const promedioAnimo = (sumaAnimo / total).toFixed(2);
    const positivos = entries.filter(e => e.nivel_animo >= 3).length;
    const tasaPositiva = Math.round((positivos / total) * 100);

    // Conteo de emociones
    const frecEmociones = {};
    entries.forEach(e => {
      const em = e.emocion || 'Estable';
      frecEmociones[em] = (frecEmociones[em] || 0) + 1;
    });

    let emocionFrecuente = 'Radiante';
    let maxConteo = 0;
    Object.entries(frecEmociones).forEach(([em, conteo]) => {
      if (conteo > maxConteo) {
        maxConteo = conteo;
        emocionFrecuente = em;
      }
    });

    return {
      total,
      promedioAnimo,
      tasaPositiva,
      rachaDias: Math.min(total, 14), // Simulación de racha consistente
      emocionFrecuente,
      distribucionEmociones: frecEmociones
    };
  };

  return (
    <MoodContext.Provider
      value={{
        entries,
        addEntry,
        updateEntry,
        deleteEntry,
        getEntryById,
        getStats
      }}
    >
      {children}
    </MoodContext.Provider>
  );
};

export const useMood = () => {
  const context = useContext(MoodContext);
  if (!context) {
    throw new Error('useMood debe utilizarse dentro de un MoodProvider');
  }
  return context;
};
