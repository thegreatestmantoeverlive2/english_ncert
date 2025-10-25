
import React, { useState, useEffect } from 'react';
import { Button, Card, CardContent, Container, Grid, Typography, Snackbar, Box } from '@mui/material';
import QuestionPalette from './QuestionPalette';

const QuizView = ({ chapter, onBack, questions: initialQuestions }) => {
    const isIncorrectQuiz = chapter === "Incorrect Questions";
    const [questions, setQuestions] = useState(initialQuestions || []);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);
    const [questionStatus, setQuestionStatus] = useState({});
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');

    useEffect(() => {
        if (!initialQuestions) {
            const fetchQuestions = async () => {
                try {
                    const response = await import(`./answers/${chapter}.json`);
                    setQuestions(response.default);
                    const savedStatus = localStorage.getItem(`quiz-status-${chapter}`);
                    if (savedStatus) {
                        setQuestionStatus(JSON.parse(savedStatus));
                    } else {
                        setQuestionStatus({});
                    }
                } catch (error) {
                    console.error("Failed to load chapter questions:", error);
                    setQuestions([]);
                }
            };

            fetchQuestions();
        }
    }, [chapter, initialQuestions]);

    useEffect(() => {
        if (!isIncorrectQuiz) {
            localStorage.setItem(`quiz-status-${chapter}`, JSON.stringify(questionStatus));
        }
    }, [questionStatus, chapter, isIncorrectQuiz]);

    const handleNextQuestion = () => {
        if (currentQuestionIndex < questions.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setShowAnswer(false);
        }
    };

    const handleShowAnswer = () => {
        setShowAnswer(true);
    };

    const handleQuestionSelect = (index) => {
        setCurrentQuestionIndex(index);
        setShowAnswer(false);
    };

    const handleStatusUpdate = (status) => {
        setQuestionStatus({
            ...questionStatus,
            [currentQuestionIndex]: status
        });
        setSnackbarMessage(`Question marked as ${status}`);
        setSnackbarOpen(true);

        if ((status === 'correct' || status === 'incorrect') && currentQuestionIndex < questions.length - 1) {
            setTimeout(() => {
                handleNextQuestion();
            }, 1000);
        }
    };

    const handleSnackbarClose = () => {
        setSnackbarOpen(false);
    };

    if (questions.length === 0) {
        return <Typography>Loading...</Typography>;
    }

    const currentQuestion = questions[currentQuestionIndex];

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 4 }}>
                <Typography variant="h4" component="h1" sx={{ color: 'var(--nord6)' }}>{chapter}</Typography>
                <Button variant="outlined" onClick={onBack} sx={{ color: 'var(--nord8)', borderColor: 'var(--nord8)' }}>Back to Chapters</Button>
            </Box>
            <Grid container spacing={4}>
                <Grid
                    size={{
                        xs: 12,
                        md: 8
                    }}>
                    <Card sx={{ backgroundColor: 'var(--nord1)', color: 'var(--nord4)', height: '100%', display: 'flex', flexDirection: 'column' }}>
                        <CardContent sx={{ flexGrow: 1 }}>
                            <Typography variant="h6" gutterBottom>Question {currentQuestionIndex + 1}</Typography>
                            <Typography variant="body1">{currentQuestion.question}</Typography>
                            {showAnswer && (
                                <Box mt={3} p={2} sx={{ backgroundColor: 'var(--nord2)', borderRadius: '4px' }}>
                                    <Typography variant="h6">Answer</Typography>
                                    <Typography variant="body1" sx={{ mt: 1 }}>{currentQuestion.answer}</Typography>
                                    {currentQuestion.extract && <Typography variant="caption" sx={{ mt: 2, display: 'block' }}><em>{currentQuestion.extract}</em></Typography>}
                                    {currentQuestion.citation && <Typography variant="caption"><small>{currentQuestion.citation}</small></Typography>}
                                </Box>
                            )}
                        </CardContent>
                    </Card>
                     <Box sx={{ mt: 2, display: 'flex', justifyContent: 'space-between' }}>
                        <div>
                            <Button variant="contained" onClick={handleShowAnswer} disabled={showAnswer} sx={{ backgroundColor: 'var(--nord10)', '&:hover': { backgroundColor: 'var(--nord9)' } }}>Show Answer</Button>
                            <Button variant="contained" onClick={handleNextQuestion} disabled={currentQuestionIndex === questions.length - 1} sx={{ ml: 2, backgroundColor: 'var(--nord10)', '&:hover': { backgroundColor: 'var(--nord9)' } }}>Next</Button>
                        </div>
                        <div>
                            <Button onClick={() => handleStatusUpdate('correct')} sx={{ color: 'var(--nord14)' }}>Correct</Button>
                            <Button onClick={() => handleStatusUpdate('incorrect')} sx={{ color: 'var(--nord11)' }}>Incorrect</Button>
                            <Button onClick={() => handleStatusUpdate('review')} sx={{ color: 'var(--nord13)' }}>Mark for Review</Button>
                        </div>
                    </Box>
                </Grid>
                <Grid
                    size={{
                        xs: 12,
                        md: 4
                    }}>
                    <QuestionPalette
                        questions={questions}
                        currentQuestionIndex={currentQuestionIndex}
                        onQuestionSelect={handleQuestionSelect}
                        questionStatus={questionStatus}
                    />
                </Grid>
            </Grid>
            <Snackbar
                open={snackbarOpen}
                autoHideDuration={2000}
                onClose={handleSnackbarClose}
                message={snackbarMessage}
                sx={{ '& .MuiSnackbarContent-root': { backgroundColor: 'var(--nord3)' } }}
            />
        </Container>
    );
};

export default QuizView;
