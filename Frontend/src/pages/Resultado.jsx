import React from 'react'
import { Typography, Button, Stack, Grid } from "@mui/material";
import { useNavigate } from 'react-router';
import { useLocation } from "react-router-dom";

export const Resultado = () => {

  const navigate = useNavigate();
  const location = useLocation();
  //Los datos llegan por el navigate
  const diabetes_result = location.state;

  return (
    <Stack justifyContent="center"> 
      <Grid container spacing={3} style={{paddingHorizontal:'20%'}} p={12}>
      <Grid item xs={12} textAlign="center">
        <Typography variant="h2">GLUCOSyS</Typography>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Typography variant='p' fontSize="19px">
          Probabilidad: {diabetes_result.probability}
        </Typography>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Typography variant='p' fontSize="19px">
          Tipo de Diabetes: {diabetes_result.type}
        </Typography>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Typography variant='p' fontSize="19px">
          Info: {diabetes_result.info}
        </Typography>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Button 
          variant="contained" 
          color="warning" 
          onClick={() => navigate("/")} 
          className={"hover-opacity"}
          sx={{
            fontSize:"1.5rem", 
            fontWeight:"bold",
            background:"var(--gradient)",
            color:"white",
            paddingX: 10,
            borderRadius: 2
          }} 
        >
          Volver al inicio
        </Button>
      </Grid>
    </Grid> 
    </Stack>  
  )
}