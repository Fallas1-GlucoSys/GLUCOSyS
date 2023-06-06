import { useState } from 'react';
import { DatosUsuarioContext } from './DatosUsuarioContext';

export const DatosUsuarioContextProvider = ({children}) => {

  const [datosUsuario, setDatosUsuario] = useState({
    'PoseeLaboratorio': "",
    'Glucemia': "",
    'Hambre':"",
    'Orina':"",
    'Peso':"",
    'Hidratacion':"",
    'AnticuerposPancreaticos': "",
    'AlientoFuerteYDulce':"",
    
  });

  return (
    <DatosUsuarioContext.Provider value={{datosUsuario, setDatosUsuario}}>
        {children}
    </DatosUsuarioContext.Provider>
  )
}
