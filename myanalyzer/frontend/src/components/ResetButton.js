import React from 'react';

import Button from '@material-ui/core/Button';



const ResetButton = ({ onClick,style})=>{

    return(
        <Button variant="contained" onClick={onClick} style={style}>
        Reset
      </Button>

    )
}

export default ResetButton;
