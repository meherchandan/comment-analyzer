import React from 'react';

import Button from '@material-ui/core/Button';



const SubmitButton = ({ onClick})=>{

    return(
        <Button variant="contained" color="primary" onClick={onClick}>
        Submit
      </Button>

    )
}

export default SubmitButton;
