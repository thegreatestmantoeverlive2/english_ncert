
import React from 'react';

const ChapterList = ({ onChapterSelect, onIncorrectQuestionsSelect }) => {
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

    return (
        <div>
            <h1>Chapters</h1>
            <button onClick={onIncorrectQuestionsSelect}>Review Incorrect Questions</button>
            <div className="chapter-grid">
                {chapters.map((chapter, index) => (
                    <div key={index} className="chapter-card" onClick={() => onChapterSelect(chapter)}>
                        <h2>{chapter}</h2>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ChapterList;
