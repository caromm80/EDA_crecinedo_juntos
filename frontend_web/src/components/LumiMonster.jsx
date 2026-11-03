import React, { useState } from 'react';

/**
 * COMPONENTE: LumiMonster
 * Mascota interactiva exclusiva del Diario de Gratitud & Mood Tracker.
 * Diseñado vectorialmente en SVG con soporte para múltiples emociones y mensajes interactivos.
 */
export const LumiMonster = ({ mood = 5, size = 180, showBubble = true, interactive = true }) => {
  const [clickCount, setClickCount] = useState(0);

  // Mensajes de sabiduría y cariño de Lumi según el nivel de ánimo (1 al 5)
  const frasesLumi = {
    5: [
      "¡Qué alegría! Tu energía radiante ilumina todo a tu alrededor.",
      "Agradecer en los días dorados multiplica la felicidad.",
      "¡Sigue brillando así! Eres increíble."
    ],
    4: [
      "La calma es el suelo fértil donde florece la gratitud.",
      "Un día sereno es un regalo precioso para el alma.",
      "Disfruta este ritmo tranquilo de tu día."
    ],
    3: [
      "Los días equilibrados nos dan espacio para respirar hondo.",
      "Incluso en la calma neutral, siempre hay una pequeña bendición.",
      "Estoy aquí contigo, acompañándote paso a paso."
    ],
    2: [
      "Es normal tener días de reflexión y pausa. No te presiones.",
      "Tus emociones son válidas. Tómate un té caliente y descansa.",
      "Lumi te recuerda: respirar lento calma el corazón."
    ],
    1: [
      "Te envío el abrazo más suave y esponjoso del mundo.",
      "Los días grises también pasan. Hoy solo concéntrate en cuidarte.",
      "Estoy muy orgulloso de ti por seguir adelante hoy."
    ]
  };

  const listaFrases = frasesLumi[mood] || frasesLumi[3];
  const fraseActual = listaFrases[clickCount % listaFrases.length];

  const handleMonsterClick = () => {
    if (interactive) {
      setClickCount(prev => prev + 1);
    }
  };

  // Configuraciones visuales según el nivel de ánimo
  const configs = {
    5: {
      colorPrincipal1: '#FF9EAA',
      colorPrincipal2: '#FFD07F',
      colorRubor: '#FB7185',
      bocaPath: 'M 65 110 Q 80 126 95 110',
      bocaFill: '#FFFFFF',
      expresionNombre: 'Lumi Radiante',
      accesorio: 'estrellas'
    },
    4: {
      colorPrincipal1: '#A7F3D0',
      colorPrincipal2: '#6EE7B7',
      colorRubor: '#34D399',
      bocaPath: 'M 68 112 Q 80 120 92 112',
      bocaFill: 'none',
      expresionNombre: 'Lumi Calmado',
      accesorio: 'flor'
    },
    3: {
      colorPrincipal1: '#DDD6FE',
      colorPrincipal2: '#C4B5FD',
      colorRubor: '#A78BFA',
      bocaPath: 'M 70 114 Q 80 118 90 114',
      bocaFill: 'none',
      expresionNombre: 'Lumi Estable',
      accesorio: 'te'
    },
    2: {
      colorPrincipal1: '#FED7AA',
      colorPrincipal2: '#FDBA74',
      colorRubor: '#FB923C',
      bocaPath: 'M 72 116 Q 80 114 88 116',
      bocaFill: 'none',
      expresionNombre: 'Lumi Pensativo',
      accesorio: 'nube'
    },
    1: {
      colorPrincipal1: '#FECDD3',
      colorPrincipal2: '#FDA4AF',
      colorRubor: '#F43F5E',
      bocaPath: 'M 70 118 Q 80 110 90 118',
      bocaFill: 'none',
      expresionNombre: 'Lumi Necesita Mimos',
      accesorio: 'manta'
    }
  };

  const config = configs[mood] || configs[3];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative' }}>
      {/* Bocadillo de diálogo cariñoso */}
      {showBubble && (
        <div
          style={{
            backgroundColor: 'var(--bg-surface)',
            border: '2px solid var(--peach-primary)',
            borderRadius: '18px',
            padding: '0.65rem 1.1rem',
            marginBottom: '0.6rem',
            maxWidth: '260px',
            fontSize: '0.85rem',
            fontWeight: '600',
            textAlign: 'center',
            color: 'var(--text-main)',
            boxShadow: 'var(--shadow-md)',
            position: 'relative',
            cursor: interactive ? 'pointer' : 'default',
            userSelect: 'none'
          }}
          onClick={handleMonsterClick}
          title="Haz clic para leer otro mensajito"
        >
          {fraseActual}
          {interactive && (
            <span style={{ display: 'block', fontSize: '0.68rem', color: 'var(--text-muted)', marginTop: '0.2rem' }}>
              (Toca a Lumi para escuchar más ✨)
            </span>
          )}
          {/* Triangulito del bocadillo */}
          <div
            style={{
              position: 'absolute',
              bottom: '-8px',
              left: '50%',
              transform: 'translateX(-50%)',
              width: 0,
              height: 0,
              borderLeft: '8px solid transparent',
              borderRight: '8px solid transparent',
              borderTop: '8px solid var(--peach-primary)'
            }}
          />
        </div>
      )}

      {/* SVG Vectorial Interactivo de Lumi */}
      <div
        onClick={handleMonsterClick}
        style={{
          cursor: interactive ? 'pointer' : 'default',
          transition: 'transform 0.25s ease',
          transform: interactive ? 'scale(1)' : 'none'
        }}
        className="animate-breathe"
      >
        <svg
          width={size}
          height={size}
          viewBox="0 0 160 160"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <linearGradient id={`lumiBody-${mood}`} x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor={config.colorPrincipal1} />
              <stop offset="100%" stopColor={config.colorPrincipal2} />
            </linearGradient>
            <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="6" stdDeviation="5" floodColor="#FB923C" floodOpacity="0.22" />
            </filter>
          </defs>

          {/* Sombra base debajo de Lumi */}
          <ellipse cx="80" cy="148" rx="46" ry="7" fill="rgba(0, 0, 0, 0.12)" />

          {/* Orejitas redondeadas y tiernas */}
          <path d="M 45 52 C 30 25, 60 18, 66 42 Z" fill={config.colorPrincipal1} filter="url(#softGlow)" />
          <path d="M 115 52 C 130 25, 100 18, 94 42 Z" fill={config.colorPrincipal1} filter="url(#softGlow)" />
          {/* Interior de orejitas */}
          <path d="M 48 48 C 38 30, 56 26, 62 42 Z" fill="#FFF5F5" opacity="0.8" />
          <path d="M 112 48 C 122 30, 104 26, 98 42 Z" fill="#FFF5F5" opacity="0.8" />

          {/* Cuerpo principal redondeado (tipo pompón monstrico) */}
          <path
            d="M 38 90 C 38 52, 122 52, 122 90 C 122 130, 106 142, 80 142 C 54 142, 38 130, 38 90 Z"
            fill={`url(#lumiBody-${mood})`}
            filter="url(#softGlow)"
          />

          {/* Pancita suave más clara */}
          <ellipse cx="80" cy="106" rx="26" ry="22" fill="#FFFFFF" opacity="0.45" />

          {/* Coloretes tiernos */}
          <ellipse cx="54" cy="98" rx="8" ry="5" fill={config.colorRubor} opacity="0.75" />
          <ellipse cx="106" cy="98" rx="8" ry="5" fill={config.colorRubor} opacity="0.75" />

          {/* Ojos según el estado de ánimo */}
          {mood === 5 && (
            <>
              {/* Ojos radiantes en arco sonriente */}
              <path d="M 54 84 Q 63 74 72 84" stroke="#1E1B4B" strokeWidth="3.5" strokeLinecap="round" fill="none" />
              <path d="M 88 84 Q 97 74 106 84" stroke="#1E1B4B" strokeWidth="3.5" strokeLinecap="round" fill="none" />
              {/* Estrellitas en los ojos */}
              <circle cx="63" cy="79" r="1.8" fill="#F59E0B" />
              <circle cx="97" cy="79" r="1.8" fill="#F59E0B" />
            </>
          )}

          {mood === 4 && (
            <>
              {/* Ojos calmos kawaii con pestañitas dulces */}
              <circle cx="63" cy="85" r="6" fill="#1E1B4B" />
              <circle cx="65" cy="83" r="2.2" fill="#FFFFFF" />
              <circle cx="61" cy="87" r="1" fill="#FFFFFF" />

              <circle cx="97" cy="85" r="6" fill="#1E1B4B" />
              <circle cx="99" cy="83" r="2.2" fill="#FFFFFF" />
              <circle cx="95" cy="87" r="1" fill="#FFFFFF" />
            </>
          )}

          {mood === 3 && (
            <>
              {/* Ojos curiosos y neutros */}
              <ellipse cx="63" cy="86" rx="5.5" ry="6.5" fill="#1E1B4B" />
              <circle cx="65" cy="84" r="2" fill="#FFFFFF" />
              <ellipse cx="97" cy="86" rx="5.5" ry="6.5" fill="#1E1B4B" />
              <circle cx="99" cy="84" r="2" fill="#FFFFFF" />
            </>
          )}

          {mood === 2 && (
            <>
              {/* Ojos pensativos mirando hacia arriba */}
              <circle cx="63" cy="85" r="5.5" fill="#1E1B4B" />
              <circle cx="63" cy="82" r="2.5" fill="#FFFFFF" />
              <circle cx="97" cy="85" r="5.5" fill="#1E1B4B" />
              <circle cx="97" cy="82" r="2.5" fill="#FFFFFF" />
              <path d="M 58 76 Q 63 74 68 76" stroke="#475569" strokeWidth="2" strokeLinecap="round" fill="none" />
            </>
          )}

          {mood === 1 && (
            <>
              {/* Ojos brillantes con lágrima tierna pidiendo apapacho */}
              <circle cx="63" cy="87" r="6.5" fill="#1E1B4B" />
              <circle cx="64" cy="85" r="3" fill="#FFFFFF" />
              <circle cx="97" cy="87" r="6.5" fill="#1E1B4B" />
              <circle cx="98" cy="85" r="3" fill="#FFFFFF" />
              {/* Lágrima suave y tierna */}
              <path d="M 105 92 Q 107 97 105 99 Q 103 97 105 92" fill="#60A5FA" opacity="0.85" />
            </>
          )}

          {/* Boquita expresiva */}
          <path
            d={config.bocaPath}
            stroke="#1E1B4B"
            strokeWidth="3"
            strokeLinecap="round"
            fill={config.bocaFill}
          />

          {/* Patitas delanteras tiernas */}
          <path d="M 52 114 C 52 122, 60 126, 66 122 Z" fill={config.colorPrincipal1} />
          <path d="M 108 114 C 108 122, 100 126, 94 122 Z" fill={config.colorPrincipal1} />

          {/* Accesorios especiales por emoción */}
          {config.accesorio === 'estrellas' && (
            <>
              <polygon points="80,26 83,34 91,35 85,41 87,49 80,45 73,49 75,41 69,35 77,34" fill="#F59E0B" />
              <circle cx="28" cy="70" r="3" fill="#FCD34D" opacity="0.9" />
              <circle cx="132" cy="72" r="3.5" fill="#FCD34D" opacity="0.9" />
            </>
          )}

          {config.accesorio === 'flor' && (
            <g transform="translate(80, 42)">
              <circle cx="-5" cy="-2" r="4" fill="#F472B6" />
              <circle cx="5" cy="-2" r="4" fill="#F472B6" />
              <circle cx="0" cy="-6" r="4" fill="#F472B6" />
              <circle cx="0" cy="2" r="4" fill="#F472B6" />
              <circle cx="0" cy="-2" r="3" fill="#FDE047" />
            </g>
          )}

          {config.accesorio === 'manta' && (
            <path
              d="M 44 116 Q 80 134 116 116 Q 80 144 44 116"
              fill="#C084FC"
              stroke="#A855F7"
              strokeWidth="2"
            />
          )}
        </svg>
      </div>

      <div style={{ marginTop: '0.4rem', fontSize: '0.8rem', fontWeight: 700, color: 'var(--peach-primary)' }}>
        {config.expresionNombre}
      </div>
    </div>
  );
};
