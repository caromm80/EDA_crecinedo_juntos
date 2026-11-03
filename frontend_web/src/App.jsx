import React from 'react';
import { RouterProvider } from 'react-router-dom';
import { router } from './routes/routes';
import { ThemeProvider } from './context/ThemeContext';
import { AuthProvider } from './context/AuthContext';
import { MoodProvider } from './context/MoodContext';

/**
 * COMPONENTE RAÍZ: App.jsx
 * Conecta los Providers de Estado Global (Context API):
 * 1. ThemeProvider: Conmutador de tema claro cálido y tema oscuro noche.
 * 2. AuthProvider: Simulación de perfil y sesión activa.
 * 3. MoodProvider: CRUD global para el diario de gratitud y estado de ánimo.
 * 4. RouterProvider: Gestor de rutas SPA definidas en routes.jsx.
 */
export function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <MoodProvider>
          <RouterProvider router={router} />
        </MoodProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
