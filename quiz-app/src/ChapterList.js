
import React from 'react';
import { Button, Card, CardContent, Container, Grid, Typography, Box } from '@mui/material';

const ChapterList = ({ onChapterSelect, onIncorrectQuestionsSelect }) => {
    const chapters = [
        "A Roadside Stand", "A Thing of Beauty", "Aunt Jennifer's Tigers", "Deep Water",
        "Going Places", "Indigo", "Journey to the end of the Earth", "Keeping Quiet",
        "Lost Spring", "Memories of Childhood", "My Mother at Sixty-six", "On The Face Of It",
        "Poets and Pancakes", "The Enemy", "The Interview", "The Last Lesson",
        "The Rattrap", "The Third Level", "The Tiger King"
    ];

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 4 }}>
                <Typography variant="h4" component="h1" sx={{ color: 'var(--nord6)' }}>
                    Chapters
                </Typography>
                <Button
                    variant="contained"
                    onClick={onIncorrectQuestionsSelect}
                    sx={{ backgroundColor: 'var(--nord10)', '&:hover': { backgroundColor: 'var(--nord9)' } }}
                >
                    Review Incorrect Questions
                </Button>
            </Box>
            <Grid container spacing={3}>
                {chapters.map((chapter, index) => (
                    <Grid
                        key={index}
                        size={{
                            xs: 12,
                            sm: 6,
                            md: 4
                        }}>
                        <Card
                            onClick={() => onChapterSelect(chapter)}
                            sx={{
                                cursor: 'pointer',
                                backgroundColor: 'var(--nord1)',
                                color: 'var(--nord4)',
                                '&:hover': { backgroundColor: 'var(--nord2)' }
                            }}
                        >
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
