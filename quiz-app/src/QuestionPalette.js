
import React from 'react';
import { Card, CardContent, Grid, Button, Typography, Box } from '@mui/material';

const QuestionPalette = ({ questions, currentQuestionIndex, onQuestionSelect, questionStatus }) => {
    const getStatusStyle = (status) => {
        if (status === 'correct') {
            return { backgroundColor: 'var(--nord14)', color: 'var(--nord0)' };
        }
        if (status === 'incorrect') {
            return { backgroundColor: 'var(--nord11)', color: 'var(--nord6)' };
        }
        if (status === 'review') {
            return { backgroundColor: 'var(--nord13)', color: 'var(--nord0)' };
        }
        return { backgroundColor: 'var(--nord3)', color: 'var(--nord5)' };
    };

    return (
        <Card sx={{ backgroundColor: 'var(--nord1)', color: 'var(--nord4)', height: '100%' }}>
            <CardContent>
                <Typography variant="h6" gutterBottom>Questions</Typography>
                <Grid container spacing={1}>
                    {questions.map((question, index) => (
                        <Grid key={index} size={3}>
                            <Button
                                variant={index === currentQuestionIndex ? 'contained' : 'outlined'}
                                onClick={() => onQuestionSelect(index)}
                                fullWidth
                                sx={{
                                    ...getStatusStyle(questionStatus[index]),
                                    borderColor: 'var(--nord4)',
                                    '&:hover': {
                                        backgroundColor: index === currentQuestionIndex ? 'var(--nord10)' : 'var(--nord2)',
                                        borderColor: 'var(--nord8)'
                                    },
                                    ...(index === currentQuestionIndex && {
                                      backgroundColor: 'var(--nord10)',
                                      color: 'var(--nord6)',
                                      borderColor: 'var(--nord10)'
                                    })
                                }}
                            >
                                {index + 1}
                            </Button>
                        </Grid>
                    ))}
                </Grid>
            </CardContent>
        </Card>
    );
};

export default QuestionPalette;
