import React, { useContext } from 'react'
import { DatosUsuarioContext } from "../../context/DatosUsuarioContext";
import {InputLabel, MenuItem, FormControl, Grid, Button, Box, Select} from '@mui/material';
import ArrowRightAltIcon from '@mui/icons-material/ArrowRightAlt';

export const Analisis = ({siguientePaso}) => {

  const {datosUsuario, setDatosUsuario} = useContext(DatosUsuarioContext);
  const setValue = (valor, key) => {
    setDatosUsuario({
      ...datosUsuario,
      [key]:valor
    });
  }
  
  return (
    <Grid container spacing={4} style={{paddingHorizontal:'20%'}}>
      <Grid item xs={12}>
        <FormControl fullWidth>
          <InputLabel id="hambre_label">¿Posee usted análisis de sangre recientes con estudios de glucemia y anticuerpos?</InputLabel>
          <Select
            labelId="analisis_previo_label"
            id="analisis_previo_select"
            value={datosUsuario.analisis_previo}
            label="¿Posee usted análisis de sangre recientes con estudios de glucemia y anticuerpos? "
            onChange={(newValue) => {
              setValue(newValue.target.value,'analisis_previo')
            }}
          >
            <MenuItem value={true}>Si</MenuItem>
            <MenuItem value={false}>No</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      {
        datosUsuario.analisis_previo == true ?
          <><Grid item xs={12}>
          <FormControl fullWidth>
            <InputLabel id="valores_glusemia_label">¿Que valores de glucemia presenta en los mismos?</InputLabel>
            <Select
              labelId="valores_glusemia_label"
              id="valores_glusemia_select"
              value={datosUsuario.valores_glusemia}
              label="¿Que valores de glucemia presenta en los mismos?"
              onChange={(newValue) => {
                setValue(newValue.target.value,'valores_glusemia')
              }}
            >
              <MenuItem value={10}>Menor a 100 mg/dL</MenuItem>
              <MenuItem value={110}>Entre 100 y 120 mg/dL</MenuItem>
              <MenuItem value={150}>Entre 120 y 180 mg/dL</MenuItem>
              <MenuItem value={190}>Mas de 180 mg/dL</MenuItem>
            </Select>
          </FormControl>
        </Grid>
  
        <Grid item xs={12}>
          <FormControl fullWidth>
            <InputLabel id="anticuarpos_label">¿Presenta anticuerpos pancreáticos?</InputLabel>
            <Select
              labelId="anticuarpos_label"
              id="anticuarpos_select"
              value={datosUsuario.anticuarpos}
              label="¿Presenta anticuerpos pancreáticos?"
              onChange={(newValue) => {
                setValue(newValue.target.value,'anticuarpos')
              }}
            >
              <MenuItem value={true}>Si</MenuItem>
              <MenuItem value={false}>No</MenuItem>
            </Select>
          </FormControl>
        </Grid>
  
  </>
        :
        <></>
      }
            
      <Grid item xs={12}>
        <Box sx={{textAlign:"center"}}>
          <Button 
            variant="contained"  
            className={"hover-opacity"}
            sx={{
              fontSize:"1.5rem", 
              fontWeight:"bold", 
              background:"var(--gradient)",
              paddingLeft:3,
              paddingRight:3,
              borderRadius:2
            }} 
            onClick={siguientePaso}
          >
            Diagnosticar
          </Button>
        </Box>
      </Grid>
    </Grid>
  )
}