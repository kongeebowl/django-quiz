export type Question = {
    id: number;
    question_text: string;
    answer: string;
}

export type Choice = {
    id: number;
    choice_text: string;
    choice_number: number;
    question: number;
}

export type Quiz = {
    id: number;
    questions: Question[];
    description: string;
    quiz_number: number;
}



