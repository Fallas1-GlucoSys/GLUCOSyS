import * as React from 'react';
import CircularProgress, {
  CircularProgressProps,
} from '@mui/material/CircularProgress';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

export function CircularProgressWithLabel(
  props
) {
  return (
    <Box sx={{ 
      position: 'relative', 
      display: 'inline-flex',
      border:"5px solid var(--secondary)",
      borderRadius:"50%"
    }}>
      <CircularProgress 
        variant="determinate" 
        {...props}
        thickness={5}
        sx = {{
          boxShadow: `inset 0 0 1px 5px white`,
          backgroundColor: 'var(--secondary)',
          borderRadius: "50%",
          color: props.colorbar
        }}
      />
      <Box
        sx={{
          top: 0,
          left: 0,
          bottom: 0,
          right: 0,
          position: 'absolute',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Typography
          variant="caption"
          component="div"
          color={props.colorbar}
          sx={{
            fontWeight:"bold",
            color: "white"
          }}
        >
          {`${Math.round(props.value)}%`}
        </Typography>
      </Box>
    </Box>
  );
}
