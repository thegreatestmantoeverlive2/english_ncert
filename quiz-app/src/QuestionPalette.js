import React from 'react';
import { Grid, Button } from '@mui/material';

const QuestionPalette = ({ questions, currentQuestionIndex, onQuestionSelect, questionStatus }) => {
    const getStatusStyle = (status) => {
        if (status === 'correct') {
            return { backgroundColor: 'green', color: 'white' };
        }
        if (status === 'incorrect') {
            return { backgroundColor: 'red', color: 'white' };
        }
        if (status === 'review') {
            return { backgroundColor: 'purple', color: 'white' };
        }
        return {};
    };

    return (
        <Grid container spacing={1}>
            {questions.map((question, index) => (
                <Grid item xs={3} key={index}>
                    <Button
                        variant={index === currentQuestionIndex ? 'contained' : 'outlined'}
                        style={getStatusStyle(questionStatus[index])}
                        onClick={() => onQuestionSelect(index)}
                        fullWidth
                    >
                        {index + 1}
                    </Button>
                </Grid>
            ))}
        </Grid>
    );
};

export default QuestionPalette;
