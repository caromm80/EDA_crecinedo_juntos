import React from 'react';

export const StatWidget = ({ title, value, subtitle, icon: Icon, color = '#FB923C', bgColor = 'rgba(251, 146, 60, 0.15)' }) => {
  return (
    <div
      className="card"
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: '1.25rem',
        padding: '1.35rem 1.5rem',
        position: 'relative',
        overflow: 'hidden'
      }}
    >
      <div
        style={{
          width: '52px',
          height: '52px',
          borderRadius: 'var(--radius-md)',
          backgroundColor: bgColor,
          color: color,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0
        }}
      >
        {Icon && <Icon size={26} />}
      </div>

      <div>
        <p style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
          {title}
        </p>
        <h3 style={{ fontSize: '1.65rem', fontWeight: 800, color: 'var(--text-main)', lineHeight: 1.15 }}>
          {value}
        </h3>
        {subtitle && (
          <p style={{ fontSize: '0.78rem', color: 'var(--text-subtle)', marginTop: '0.2rem' }}>
            {subtitle}
          </p>
        )}
      </div>
    </div>
  );
};
