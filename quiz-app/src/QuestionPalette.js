
import React from 'react';

const QuestionPalette = ({ questions, currentQuestionIndex, onQuestionSelect, questionStatus }) => {
    const getStatusClass = (status) => {
        if (status === 'correct') {
            return 'correct';
        }
        if (status === 'incorrect') {
            return 'incorrect';
        }
        if (status === 'review') {
            return 'review';
        }
        return '';
    };

    return (
        <div className="question-palette">
            {questions.map((question, index) => (
                <div
                    key={index}
                    className={`palette-item ${index === currentQuestionIndex ? 'active' : ''} ${getStatusClass(questionStatus[index])}`}
                    onClick={() => onQuestionSelect(index)}
                >
                    {index + 1}
                </div>
            ))}
        </div>
    );
};

export default QuestionPalette;
