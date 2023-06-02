import React from "react"

export const CustomCard = ( { content, title, titleSize } ) => {
  return (
    <div style={{
      boxShadow: "0px 2px 4px 1px rgba(0, 0, 0, 0.5)",
      borderRadius:"10px",
      marginLeft: "2%",
      marginRight: "2%"
    }}>
      <div 
        style={{
          borderTopLeftRadius:"10px",
          borderTopRightRadius:"10px",
          borderTop:"15px solid transparent", 
          borderImageSource:"var(--gradient)",
          background: "var(--gradient) border-box",
          minHeight:20
        }}
      >
        {
        title ?
          <h2 style={{
            padding: "0.75rem",
            paddingTop: 0,
            margin: 0,
            color: "white",
            fontWeight: "bold",
            fontSize: titleSize
          }}>
            {title.toUpperCase()}
          </h2>
          : 
          <></>    
        }
        
      </div>
      <div
        style={{
          padding:"1rem",
          paddingTop:"2rem",
          background: "lightgray",
          filter: "brightness(108%)"
        }}
      >
        { content }
      </div>
    </div>
  )
}
