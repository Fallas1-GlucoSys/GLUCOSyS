import React, {useContext, useState}from 'react';
import { CustomCard } from '../components/CustomCard'
import { CustomStepper } from '../components/CustomStepper'
import { Sintomas } from '../components/Steps/Sintomas'
import { Analisis } from '../components/Steps/Analisis'
import { Alert, Button, Grid, Dialog, DialogTitle, DialogContent, DialogActions, DialogContentText } from '@mui/material';
import { useNavigate } from 'react-router';
import { DatosUsuarioContext } from '../context/DatosUsuarioContext';
import KeyboardBackspaceIcon from '@mui/icons-material/KeyboardBackspace';

export const PasosForm = () => {

  const navigate = useNavigate();
  const [datosError, setDatosError] = useState("");
  const [pasoActual, setPasoActual] = React.useState(0);
  const {datosUsuario} = useContext(DatosUsuarioContext);
  
  const titulosSecciones = [
    "Sintomatología",
    "Análisis de Laboratorio"
  ];
  const [toggle, setToggle] = useState(false)
  const submitForm = async () => {
    //TODO: call endpoint
    //Guardar en esta variable el resultado del endpoint...
    const resultEngine = undefined;
    navigate("/result", resultEngine);
  }
  const validarDatos = () => {
    let valido = true;
    let errorMessagge = 'Faltan completar los sigueintes campos: ';
    if(!datosUsuario.hambre){
      valido = false;
      errorMessagge += 'si ha tenido hambre'
    }
    if(!datosUsuario.orina){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'frecuencia de orina'
    }
    if(!datosUsuario.peso){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'cambio de peso'
    }
    if(!datosUsuario.hidratacion){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'datos de hidratacion'
    }
    if(!datosUsuario.aliento){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'sobre su aliento'
    }
    if(!datosUsuario.glucemia){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'datos sobre glusemia'
    }
    if(!datosUsuario.anticuerpos_pancreaticos){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'anticuerpos pancreaticos'
    }
    if(datosUsuario.analisis_previo && !datosUsuario.valores_glusemia){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'valores de glusemia'
    }
    if(datosUsuario.analisis_previo && !datosUsuario.anticuarpos){
      if(!valido)errorMessagge += ', ';
      valido = false;
      errorMessagge += 'anticuerpos'
    }
    errorMessagge += '.'
    return valido, errorMessagge;
  }
  const siguientePaso = () => {
    if (pasoActual === 1){
      let result, message = validarDatos();
      if(result){
        submitForm();
      }else{
        setToggle(true);
        setDatosError(message);
      }
      
      
    } else{
      setPasoActual((pasoActual) => pasoActual + 1);
    }
  }

  const pasoAnterior = () => {
    if (pasoActual === 0){
      navigate("/");
    }else{
      setPasoActual((pasoActual) => pasoActual - 1);
    }
  }

  const componentesSecciones = [
    <Sintomas siguientePaso={siguientePaso}/>,
    <Analisis siguientePaso={siguientePaso}/>
  ];

  return (
    
    <>
      <Grid container>
        <Grid xs={12} item style={{display:"flex", justifyContent:"center"}}>
          <img src="logo.png" alt="Logo" width="200"/>
        </Grid>
      </Grid>
      <Grid container spacing={1} alignItems="center" justifyContent="center">
        <Grid item xs={12} md={3} lg={2} xl={1} style={{textAlign:"center", verticalAlign:"center"}}>
          <Button   
            className={"hover-opacity"}
            sx={{
              fontSize:"1.5rem", 
              fontWeight:"bold", 
              backgroundColor:"lightgray",
              background:"lightgray",
              color:"black",
              border: "2px solid var(--primary)",
              paddingLeft:3,
              paddingRight:3,
              borderRadius:2,
              filter: "brightness(108%)"
            }} 
            onClick={pasoAnterior}
          >
            <KeyboardBackspaceIcon
              style={{
                fontSize:"2rem",
                marginRight:15
              }}
            />
            Volver
          </Button>
        </Grid>
      <Grid item xs={12} md={9} lg={10} xl={11}>
        <CustomStepper
          currentStep={pasoActual}
          steps={titulosSecciones}
        />
      </Grid>
      </Grid>
      <CustomCard 
          title={titulosSecciones[pasoActual]}
          content={
            componentesSecciones[pasoActual]
          }
      />
      <Dialog
        open={toggle}
        
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {"Faltan completar datos"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {datosError}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => { setToggle(false)}} autoFocus>
            Aceptar
          </Button>
        </DialogActions>
      </Dialog>
    </>
  )
}
