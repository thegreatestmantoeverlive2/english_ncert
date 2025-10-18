
import React, { useState } from 'react';
import './App.css';
import ChapterList from './ChapterList';
import QuizView from './QuizView';

function App() {
  const [selectedChapter, setSelectedChapter] = useState(null);
  const [incorrectQuestions, setIncorrectQuestions] = useState([]);
  const [isIncorrectQuiz, setIsIncorrectQuiz] = useState(false);

  const handleChapterSelect = (chapter) => {
    setSelectedChapter(chapter);
    setIsIncorrectQuiz(false);
  };

  const handleIncorrectQuestionsSelect = () => {
    const allIncorrectQuestions = [];
    const chapters = [
        "A Roadside Stand",
        "A Thing of Beauty",
        "Aunt Jennifer's Tigers",
        "Deep Water",
        "Going Places",
        "Indigo",
        "Journey to the end of the Earth",
        "Keeping Quiet",
        "Lost Spring",
        "Memories of Childhood",
        "My Mother at Sixty-six",
        "On The Face Of It",
        "Poets and Pancakes",
        "The Enemy",
        "The Interview",
        "The Last Lesson",
        "The Rattrap",
        "The Third Level",
        "The Tiger King"
    ];

    chapters.forEach(chapter => {
      const savedStatus = localStorage.getItem(`quiz-status-${chapter}`);
      if (savedStatus) {
        const statuses = JSON.parse(savedStatus);
        const chapterQuestions = require(`./answers/${chapter}.json`);
        Object.keys(statuses).forEach(index => {
          if (statuses[index] === 'incorrect') {
            allIncorrectQuestions.push(chapterQuestions[index]);
          }
        });
      }
    });

    setSelectedChapter("Incorrect Questions");
    setIncorrectQuestions(allIncorrectQuestions);
    setIsIncorrectQuiz(true);
  };

  const handleBackToChapters = () => {
    setSelectedChapter(null);
    setIsIncorrectQuiz(false);
  };

  return (
    <div className="App">
      {selectedChapter ? (
        <QuizView
          chapter={selectedChapter}
          onBack={handleBackToChapters}
          questions={isIncorrectQuiz ? incorrectQuestions : null}
        />
      ) : (
        <ChapterList
          onChapterSelect={handleChapterSelect}
          onIncorrectQuestionsSelect={handleIncorrectQuestionsSelect}
        />
      )}
    </div>
  );
}

export default App;
