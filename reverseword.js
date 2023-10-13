#javascript code to Take a sentence as an input and reverse every word in that sentence.
function reverseWordsInSentence(sentence) {
    // Split the sentence into words
    const words = sentence.split(' ');

    // Reverse each word
    const reversedWords = words.map(word => reverseWord(word));

    // Join the reversed words back into a sentence
    const reversedSentence = reversedWords.join(' ');

    return reversedSentence;
}

function reverseWord(word) {
    // Split the word into an array of characters, reverse it, and join it back together
    return word.split('').reverse().join('');
}

// Example usage
const inputSentence = "This is a sunny day";
const reversedSentence = reverseWordsInSentence(inputSentence);

console.log(reversedSentence);
