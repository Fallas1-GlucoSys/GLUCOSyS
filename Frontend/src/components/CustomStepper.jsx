import { Stepper, Step, StepLabel } from "@mui/material";
import { CircularProgressWithLabel } from "./CircularProgressWithLabel";
import React from "react";

export const CustomStepper = ( 
  { 
    currentStep, 
    steps
  }
) => {
  const completedColor = "var(--primary)";
  const activeColor = "var(--secondary)";
  
  const stepStyle = {
    "& .Mui-active": {
      "&.MuiStepIcon-root": {
        color: activeColor,
      },
      "& .MuiStepConnector-line": {
        borderColor: activeColor
      }
    },
    "& .Mui-completed": {
      "&.MuiStepIcon-root": {
        color: completedColor,
      },
      "& .MuiStepConnector-line": {
        borderColor: completedColor
      }
    }
  }

  return (
    <div style={{
      display:"flex", 
      justifyContent:"center", 
      alignContent:"center",
      marginTop: "1.5rem",
      marginBottom: "1.5rem"
    }}>
      <Stepper 
        activeStep={currentStep} 
        alternativeLabel 
        sx={{
          ...stepStyle,
          width:"80%",
          borderRadius: "10px",
          boxShadow: "0px 2px 4px 1px rgba(0, 0, 0, 0.5)",
          paddingTop: "0.5rem",
          paddingBottom: "0.5rem",
          background: "lightgray",
          filter: "brightness(108%)"
        }}
        className={"stepper"}
      >
        {steps.map((step) => (
          <Step key={step}>
            <StepLabel>
              {step}
            </StepLabel>
          </Step>
        ))}
      </Stepper>
      <div style={{
        display:"flex",
        justifyContent:"center", 
        alignContent:"center",
        marginLeft:"2rem",
        marginTop:"auto",
        paddingTop: "0.5rem",
        paddingBottom: "0.5rem"
      }}>
        <CircularProgressWithLabel 
          value={(currentStep)*100/steps.length}
          colorbar={completedColor}
        />
      </div>
    </div>
  )
}
