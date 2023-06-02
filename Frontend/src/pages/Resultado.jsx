import React from 'react'
import { Container, Box, Typography, Button, Stack, Grid } from "@mui/material";
import { useNavigate } from 'react-router';

export const Resultado = () => {

  const navigate = useNavigate();

  return (
    <Stack justifyContent="center"> 
      <Grid container spacing={3} style={{paddingHorizontal:'20%'}} p={12}>
      <Grid item xs={12} textAlign="center">
        <Typography variant="h2">GLUCOSyS</Typography>
      </Grid>
      <Grid item xs={12} textAlign="center">
        <Typography variant='p' fontSize="19px">
          TODO
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