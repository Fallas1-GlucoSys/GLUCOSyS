import { useState, useContext } from 'react';
import { DatosUsuarioContext } from './DatosUsuarioContext';

export const DatosUsuarioContextProvider = ({children}) => {

  const [datosUsuario, setDatosUsuario] = useState({
      // 'hambre':false,
      // 'orina':false,
      // 'peso':false,
      // 'hidratacion':true,
      // 'aliento':true,
      // 'glucemia': undefined,
      // 'anticuerpos_pancreaticos': false
  });

  return (
    <DatosUsuarioContext.Provider value={{datosUsuario, setDatosUsuario}}>
        {children}
    </DatosUsuarioContext.Provider>
  )
}
