import React from 'react'
import { useNavigate } from "react-router-dom";
import { Stack, Box, Button, Grid, Typography } from '@mui/material';

export const Home = () => {
  const navigate = useNavigate();
  return (
    <Stack justifyContent="center"> 
      <Grid container spacing={3} style={{paddingHorizontal:'20%'}} p={12}>
      <Grid item xs={12} textAlign="center">
        <img src="logo.png" alt="Logo" width="450"/>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <div style={{minWidth:280, width:"60%", margin:"auto"}}>
          <Typography variant='p' fontSize="19px">
            El presente sistema experto se desarrolló para efectuar diagnósticos presuntivos de diabetes. Si usted cree que posee o desea conocer si existe la posibilidad de poseer algún tipo de diabetes, puede llenar nuestro cuestionario y obtendrá una respuesta al instante.
          </Typography>
        </div>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Button 
          variant="contained" 
          color="warning" 
          className={"hover-opacity"}
          onClick={() => navigate("/form")} 
          sx={{
            fontSize:"1.5rem", 
            fontWeight:"bold",
            background:"var(--gradient)",
            color:"white",
            paddingX: 10,
            borderRadius: 2
          }} >
            Diagnosticar
          </Button>
      </Grid>
    </Grid> 
    </Stack> 
  )
}