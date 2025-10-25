
import React, { useState, useEffect } from 'react';
import QuestionPalette from './QuestionPalette';

const QuizView = ({ chapter, onBack, questions: initialQuestions }) => {
    const isIncorrectQuiz = chapter === "Incorrect Questions";
    const [questions, setQuestions] = useState(initialQuestions || []);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);
    const [questionStatus, setQuestionStatus] = useState({});

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
    };

    if (questions.length === 0) {
        return <div>Loading...</div>;
    }

    const currentQuestion = questions[currentQuestionIndex];

    return (
        <div>
            <button onClick={onBack}>Back to Chapters</button>
            <h1>{chapter}</h1>
            <div className="quiz-container">
                <div className="quiz-card">
                    <h2>{currentQuestion.question}</h2>
                    {showAnswer && (
                        <div>
                            <p>{currentQuestion.answer}</p>
                            <p><em>{currentQuestion.extract}</em></p>
                            <p><small>{currentQuestion.citation}</small></p>
                        </div>
                    )}
                </div>
                <QuestionPalette
                    questions={questions}
                    currentQuestionIndex={currentQuestionIndex}
                    onQuestionSelect={handleQuestionSelect}
                    questionStatus={questionStatus}
                />
            </div>
            <button onClick={handleShowAnswer} disabled={showAnswer}>Show Answer</button>
            <button onClick={handleNextQuestion} disabled={currentQuestionIndex === questions.length - 1}>Next</button>
            <div>
                <button onClick={() => handleStatusUpdate('correct')}>Correct</button>
                <button onClick={() => handleStatusUpdate('incorrect')}>Incorrect</button>
                <button onClick={() => handleStatusUpdate('review')}>Mark for Review</button>
            </div>
        </div>
    );
};

export default QuizView;
