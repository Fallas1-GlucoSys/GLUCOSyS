import React from 'react';
import * as ReactDOM from 'react-dom/client';
import "./general.css"
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import { Home } from './pages/Home';
import { DynamicForm } from './pages/DynamicForm';
import { Resultado } from './pages/Resultado';
import { DatosUsuarioContextProvider } from './context/DatosUsuarioContextProvider';

const root = ReactDOM.createRoot(document.getElementById('root'));

const router = createBrowserRouter([
  {path:"/", element:<Home/>},
  {
    path:"/form", 
    element:
    <DatosUsuarioContextProvider children={
      <DynamicForm/>
    }/>
  },
  {path:"/result", element:<Resultado/>},

]);
root.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);
