import React from 'react';
import { createBrowserRouter, Navigate } from 'react-router-dom';
import { MainLayout } from '../layouts/MainLayout';
import { AuthLayout } from '../layouts/AuthLayout';
import { DashboardView } from '../views/DashboardView';
import { EntriesListView } from '../views/EntriesListView';
import { CreateEntryView } from '../views/CreateEntryView';
import { EditEntryView } from '../views/EditEntryView';
import { UsersListView } from '../views/UsersListView';
import { LoginView } from '../views/LoginView';
import { AboutView } from '../views/AboutView';

/**
 * ARCHIVO REQUERIDO: routes.jsx
 * Configuración central de enrutamiento SPA (React Router DOM v7).
 * Permite la navegación fluida entre vistas sin recarga de página (Semana 7).
 * Gestiona MainLayout para la aplicación y AuthLayout para login/onboarding.
 */
export const router = createBrowserRouter([
  {
    path: '/',
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: <Navigate to="/dashboard" replace />
      },
      {
        path: 'dashboard',
        element: <DashboardView />
      },
      {
        path: 'diario',
        element: <EntriesListView />
      },
      {
        path: 'nueva-entrada',
        element: <CreateEntryView />
      },
      {
        path: 'editar/:id',
        element: <EditEntryView />
      },
      {
        path: 'usuarios',
        element: <UsersListView />
      },
      {
        path: 'acerca-de',
        element: <AboutView />
      }
    ]
  },
  {
    element: <AuthLayout />,
    children: [
      {
        path: 'login',
        element: <LoginView />
      }
    ]
  },
  {
    path: '*',
    element: <Navigate to="/dashboard" replace />
  }
]);
