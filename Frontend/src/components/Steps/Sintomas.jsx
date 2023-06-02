import React, {useContext,useState} from 'react';
import {InputLabel, MenuItem, FormControl, Grid, Button, Box, Select} from '@mui/material';
import { DatosUsuarioContext } from '../../context/DatosUsuarioContext';
import ArrowRightAltIcon from '@mui/icons-material/ArrowRightAlt';


export const Sintomas = ({siguientePaso}) => {

  const {datosUsuario, setDatosUsuario} = useContext(DatosUsuarioContext);
  const setValue = (valor, key) => {
    console.log(key);
    setDatosUsuario({
      ...datosUsuario,
      [key]:valor
    });
  }
  
  return (
    <Grid container spacing={4} style={{paddingHorizontal:'20%'}}>
      <Grid item xs={12}>
        <FormControl required fullWidth>
          <InputLabel id="hambre_label">¿Con qué frecuencia tienes hambre?</InputLabel>
          <Select 
            labelId="hambre_label"
            id="hambre_select"
            value={datosUsuario.hambre}
            label="¿Con qué frecuencia tienes hambre? "
            onChange={(newValue) => {
              setValue(newValue.target.value,'hambre')
            }}
          >
            <MenuItem value={true}>Frecuente</MenuItem>
            <MenuItem value={false}>Normal o poca</MenuItem>
          </Select>
        </FormControl>
      </Grid>

      <Grid item xs={12}>
        <FormControl required fullWidth>
          <InputLabel id="orina_label">¿Con qué frecuencia orinas?</InputLabel>
          <Select 
            labelId="orina_label"
            id="orina_select"
            value={datosUsuario.orina}
            label="¿Con qué frecuencia orinas?"
            onChange={(newValue) => {
              setValue(newValue.target.value,'orina')
            }}
          >
            <MenuItem value={true}>Frecuente</MenuItem>
            <MenuItem value={false}>Usual o Escasa</MenuItem>
          </Select>
        </FormControl>
      </Grid>

      <Grid item xs={12}>
        <FormControl required fullWidth>
          <InputLabel id="peso_label">¿Cómo encuentras tu pérdida de peso?</InputLabel>
          <Select 
            labelId="peso_label"
            id="peso_select"
            value={datosUsuario.peso}
            label="¿Cómo encuentras tu pérdida de peso?"
            onChange={(newValue) => {
              setValue(newValue.target.value,'peso')
            }}
          >
            <MenuItem value={true}>Sostenida sin causa</MenuItem>
            <MenuItem value={false}>Normal</MenuItem>
          </Select>
        </FormControl>
      </Grid>

      <Grid item xs={12}>
        <FormControl required fullWidth>
          <InputLabel id="hidratacion_label">¿Cómo se siente usualmente en cuanto a hidratación?</InputLabel>
          <Select 
            labelId="hidratacion_label"
            id="hidratacion_select"
            value={datosUsuario.hidratacion}
            label="¿Cómo se siente usualmente en cuanto a hidratación?"
            onChange={(newValue) => {
              setValue(newValue.target.value,'hidratacion')
            }}
          >
            <MenuItem value={true}>Sed Frecuente</MenuItem>
            <MenuItem value={false}>Hidratado</MenuItem>
          </Select>
        </FormControl>
      </Grid>

      <Grid item xs={12}>
        <FormControl required fullWidth>
          <InputLabel id="hambre_label">Usted describiría a su aliento como...</InputLabel>
          <Select 
            labelId="aliento_label"
            id="aliento_select"
            value={datosUsuario.aliento}
            label="Usted describiría a su aliento como... "
            onChange={(newValue) => {
              setValue(newValue.target.value,'aliento')
            }}
          >
            <MenuItem value={true}>Fuerte y Dulce</MenuItem>
            <MenuItem value={false}>Otra</MenuItem>
          </Select>
        </FormControl>
      </Grid>
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
            Siguiente
            <ArrowRightAltIcon
              style={{
                fontSize:"3rem",
                marginLeft:15
              }}
            />
          </Button>
        </Box>
      </Grid>
    </Grid>
  )
}