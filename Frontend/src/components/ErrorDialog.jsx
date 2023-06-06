import React from 'react'
import { Dialog, DialogContent, DialogContentText, DialogActions, DialogTitle, Button } from '@mui/material';

export const ErrorDialog = ({error}) => {

  const [open, setOpen] = React.useState(false);

  React.useEffect(() => {
    if(error && error !== ""){
      setOpen(true);
    }else{
      setOpen(false);
    }

  },[error]);

  const handleClose = () => {
    setOpen(false);
  }

  return (
    <Dialog
      fullWidth={true}
      maxWidth={"sm"}
      open={open}
      onClose={handleClose}
    >
      <DialogTitle>Error</DialogTitle>
      <DialogContent>
        <DialogContentText>
          {error}
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Close</Button>
      </DialogActions>
    </Dialog>
  )
}
