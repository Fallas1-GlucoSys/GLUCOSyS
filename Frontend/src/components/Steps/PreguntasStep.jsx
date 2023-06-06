import React from 'react'
import { DatosUsuarioContext } from '../../context/DatosUsuarioContext';
import {InputLabel, MenuItem, FormControl, Grid, Select} from '@mui/material';

export const PreguntasStep = ( {questions} ) => {

  const [stateQuestions, setStateQuestions] = React.useState([]);
  const {datosUsuario, setDatosUsuario} = React.useContext(DatosUsuarioContext);

  React.useEffect(() => {
    setStateQuestions(questions);
  }, [questions]);

  return (
    <Grid container spacing={4} style={{paddingHorizontal:'20%'}}>
      {stateQuestions.map((question, idx) => {return(
        <Grid item xs={12} key={`${question.field}_${idx}`}>
          <FormControl required fullWidth>
            <InputLabel id={`${question.field}_label`}>{question.question}</InputLabel>
            <Select 
              labelId={`${question.field}_label`}
              id={`${question.field}_select`}
              label={question.question}
              value={datosUsuario[question.field]}
              onChange={(newValue) => {
                setDatosUsuario({
                  ...datosUsuario,
                  [question.field]: newValue.target.value
                });
              }}
            >
              {question.options.map((option, idx) => {return(
                <MenuItem key={`${option.text_to_show}_${option.value}_${idx}`}value={option.value}>{option.text_to_show}</MenuItem>
              )})}
            </Select>
          </FormControl>
        </Grid>
      );
      })}
    </Grid>
  )
}
