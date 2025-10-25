
import React, { useState, useEffect } from 'react';
import { Button, Card, CardContent, Container, Grid, Typography, Snackbar } from '@mui/material';
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
        <Container>
            <Button variant="outlined" onClick={onBack} style={{ margin: '20px 0' }}>Back to Chapters</Button>
            <Typography variant="h4" component="h1" gutterBottom>{chapter}</Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} md={8}>
                    <Card>
                        <CardContent>
                            <Typography variant="h6">{currentQuestion.question}</Typography>
                            {showAnswer && (
                                <div>
                                    <Typography variant="body1">{currentQuestion.answer}</Typography>
                                    <Typography variant="caption"><em>{currentQuestion.extract}</em></Typography>
                                    <Typography variant="caption"><small>{currentQuestion.citation}</small></Typography>
                                </div>
                            )}
                        </CardContent>
                    </Card>
                    <div style={{ marginTop: '20px' }}>
                        <Button variant="contained" onClick={handleShowAnswer} disabled={showAnswer}>Show Answer</Button>
                        <Button variant="contained" color="primary" onClick={handleNextQuestion} disabled={currentQuestionIndex === questions.length - 1} style={{ marginLeft: '10px' }}>Next</Button>
                    </div>
                    <div style={{ marginTop: '20px' }}>
                        <Button onClick={() => handleStatusUpdate('correct')}>Correct</Button>
                        <Button onClick={() => handleStatusUpdate('incorrect')}>Incorrect</Button>
                        <Button onClick={() => handleStatusUpdate('review')}>Mark for Review</Button>
                    </div>
                </Grid>
                <Grid item xs={12} md={4}>
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
            />
        </Container>
    );
};

export default QuizView;
