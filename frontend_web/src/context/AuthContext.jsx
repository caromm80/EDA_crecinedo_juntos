import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem('lumi_user');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        console.error(e);
      }
    }
    // Usuario por defecto conectado para pruebas inmediatas
    return {
      id: 1,
      nombre: 'Carolina Morales',
      email: 'carolina@cesde.edu.co',
      rol: 'Estudiante & Exploradora Emocional',
      avatarMonster: 'lumi_happy',
      diasActivo: 14,
      isLoggedIn: true
    };
  });

  useEffect(() => {
    if (user) {
      localStorage.setItem('lumi_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('lumi_user');
    }
  }, [user]);

  const login = (nombre, email) => {
    const newUser = {
      id: Date.now(),
      nombre: nombre.trim() || 'Amigo de Lumi',
      email: email.trim() || 'usuario@lumi.app',
      rol: 'Miembro de la Comunidad',
      avatarMonster: 'lumi_happy',
      diasActivo: 1,
      isLoggedIn: true
    };
    setUser(newUser);
    return true;
  };

  const logout = () => {
    setUser({
      id: null,
      nombre: 'Invitado',
      email: '',
      rol: 'Visitante',
      avatarMonster: 'lumi_calm',
      diasActivo: 0,
      isLoggedIn: false
    });
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, isAuthenticated: !!user?.isLoggedIn }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth debe usarse dentro de un AuthProvider');
  }
  return context;
};
