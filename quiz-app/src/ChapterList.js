import React from 'react';
import { Button, Card, CardContent, Container, Grid, Typography } from '@mui/material';

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
        <Container>
            <Typography variant="h4" component="h1" gutterBottom>
                Chapters
            </Typography>
            <Button variant="contained" color="primary" onClick={onIncorrectQuestionsSelect} style={{ marginBottom: '20px' }}>
                Review Incorrect Questions
            </Button>
            <Grid container spacing={3}>
                {chapters.map((chapter, index) => (
                    <Grid item xs={12} sm={6} md={4} key={index}>
                        <Card onClick={() => onChapterSelect(chapter)} style={{ cursor: 'pointer' }}>
                            <CardContent>
                                <Typography variant="h6" component="h2">
                                    {chapter}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
};

export default ChapterList;
