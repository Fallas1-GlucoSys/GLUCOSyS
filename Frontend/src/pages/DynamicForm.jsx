import React from 'react'
import { CustomCard } from '../components/CustomCard'
import { CustomStepper } from '../components/CustomStepper'
import { Button, Grid, Box } from '@mui/material';
import { PreguntasStep } from '../components/Steps/PreguntasStep';
import { DatosUsuarioContext } from '../context/DatosUsuarioContext';
import KeyboardBackspaceIcon from '@mui/icons-material/KeyboardBackspace';
import { useNavigate } from 'react-router';
import ArrowRightAltIcon from '@mui/icons-material/ArrowRightAlt';
import { ErrorDialog } from '../components/ErrorDialog';

const titulosSecciones = [
  "Formulario",
  "Resultado"
];

export const DynamicForm = () => {

  const pasoActual = 0;
  const [historyQuestions, setHistoryQuestions] = React.useState([
    {questions: [], data:{}}
  ]);
  const [questionStep, setQuestionStep] = React.useState(0);
  const [questionsCurrentStep, setQuestionsCurrentStep] = React.useState([{
    question: "¿Posee usted análisis de sangre recientes con estudios de glucemia y anticuerpos?",
    field: "PoseeLaboratorio",
    options: [
      {value: true, text_to_show:"Sí, poseo"},
      {value: false, text_to_show:"No, no poseo"}
    ]
  }]);
  const [error, setError] = React.useState();
  const {datosUsuario, setDatosUsuario} = React.useContext(DatosUsuarioContext);
  const navigate = useNavigate();

  const pasoAnterior = () => {
    if (questionStep > 0){
      const data = historyQuestions[questionStep-1];
      setQuestionStep(questionStep - 1);
      setQuestionsCurrentStep(data.questions);
      setDatosUsuario(data.data);
    }else{
      navigate("/");
    }
  }

  const validateDatosUsuarioHasAllNewFields = () => {
    for (let i=0; i<questionsCurrentStep.length; i++){
      if (!(questionsCurrentStep[i].field in datosUsuario) || datosUsuario[questionsCurrentStep[i].field] === ""){
        return false;
      }
    }
    return true;
  }

  const fetchNextStep = async () => {
    const response = await fetch(
      "http://localhost:3100/diabetes_probability",
      {
        method:"POST",
        headers: {
          "Content-Type": "application/json",
        },
        //Filtro los empty strings. No tiene sentido mandarlos.
        body: JSON.stringify(Object.fromEntries(Object.entries(datosUsuario).filter(([_, v]) => v != null && v != undefined && v !== "")))
      }
    );
    if (response.status !== 200){
      setError(response.statusText);
      return;
    }
    const json_response = await response.json();
    if (json_response.response_type === "QUESTIONS"){
      setQuestionsCurrentStep(json_response.questions);
    }else{
      navigate("/result", {state:json_response})
    }
  }

  const validarPoseeLaboratorio = () => {
    if (!("PoseeLaboratorio" in datosUsuario)){
      
      return false;
    }else if (datosUsuario["PoseeLaboratorio"] === false){
      navigate("/result", {state:{
        response_type: "RESULT", 
        type:"Indefinido", 
        probability:"Indefinida", 
        info:"No se puede obtener un resultado sin poseer estudios de laboratorio. Lo sentimos."
      }});
    }
    return true;
  }

  const pasoSiguiente = () => {
    if (questionStep === 0 && !validarPoseeLaboratorio()){
      setError("Debe rellenar todos los campos antes de continuar.");
      return;
    }
    if (validateDatosUsuarioHasAllNewFields()){
      let newHistoryQuestions = [
        ...historyQuestions
      ];
      newHistoryQuestions[questionStep] = {
        questions: questionsCurrentStep,
        data: datosUsuario,
      };
      setHistoryQuestions(newHistoryQuestions);
      setQuestionStep(questionStep + 1);
      fetchNextStep();
    }else{
      setError("Debe rellenar todos los campos antes de continuar.");
    }
    
  }

  return (
    <>
      <ErrorDialog error={error}/>
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
            <PreguntasStep 
              questions={questionsCurrentStep} 
              initialResponses={historyQuestions.length > questionStep ? historyQuestions[questionStep] : []}
            />
          }
      />
      <Box sx={{textAlign:"center", marginTop:"1rem"}}>
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
          onClick={pasoSiguiente}
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
    </>
  )
}
