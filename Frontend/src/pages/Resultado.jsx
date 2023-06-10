import React from "react";
import { Typography, Button, Stack, Grid, Chip, Box } from "@mui/material";
import { useNavigate } from "react-router";
import { useLocation } from "react-router-dom";

const color_proba = {
  Nula: "success",
  Baja: "primary",
  Media: "warning",
  Alta: "error",
};

const color_type = {
  "Tipo 1": "#4db6ac",
  "Tipo 2": "#9575cd",
  Ninguno: "#d7ccc8",
};

export const Resultado = () => {
  const navigate = useNavigate();
  const location = useLocation();
  //Los datos llegan por el navigate
  const diabetes_result = location.state;

  return (
    <Stack justifyContent="center">
      <Grid container spacing={3} style={{ paddingHorizontal: "20%" }} p={12}>
        <Grid item xs={12} textAlign="center">
          <img src="logo.png" alt="Logo" width="450" />
        </Grid>
        <Grid item xs={12} textAlign="center">
          <Stack
            direction="row"
            spacing={1}
            alignItems="center"
            justifyContent="center"
          >
            <Typography variant="h3">Tipo de Diabetes:</Typography>
            <span
              style={{
                backgroundColor: color_type[diabetes_result.type],
                padding: "0 10px 0 10px",
                borderRadius: 4,
              }}
            >
              <Typography variant="h3">{diabetes_result.type}</Typography>
            </span>
          </Stack>
        </Grid>

        <Grid item xs={12} textAlign="center">
          <Stack
            direction="row"
            spacing={1}
            alignItems="center"
            justifyContent="center"
          >
            <Chip
              label={`Probabilidad - ${diabetes_result.probability}`}
              color={color_proba[diabetes_result.probability]}
              classes={{
                root: "chip-proba",
              }}
            />
          </Stack>
        </Grid>
        <Grid item xs={12} textAlign="center">
          <Box
            sx={{
              p: 3,
              display: "span",
              bgcolor: "#e1f5fe",
              borderRadius: 1,
            }}
          >
            <Typography
              component="p"
              variant="p"
              fontSize="18px"
              fontStyle="italic"
              dangerouslySetInnerHTML={{ __html: diabetes_result.info }}
            ></Typography>
          </Box>
        </Grid>
        <Grid item xs={12} textAlign="center">
          <Button
            variant="contained"
            color="warning"
            onClick={() => navigate("/")}
            className={"hover-opacity"}
            sx={{
              fontSize: "1.5rem",
              fontWeight: "bold",
              background: "var(--gradient)",
              color: "white",
              paddingX: 10,
              borderRadius: 2,
            }}
          >
            Volver al inicio
          </Button>
        </Grid>
      </Grid>
    </Stack>
  );
};
