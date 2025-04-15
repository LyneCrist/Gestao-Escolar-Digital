"use strict";

const isAlpha = /[^A-Za-z\u00C0-\u00FF\s\b]/g;

const isNumeric = /[^0-9\b]/g;

const isAlphaNumeric = /[^A-Za-z0-9.-]/g;

const isAlphaNumericCharacter = /[^A-Za-z0-9\u00C0-\u00FF._-\s\b]/g;

function maskPhone(text) {

    const cleanText = text.replace(/\D/g, "");

    const numbers = (cleanText.substring(0, 2) === "55") ? cleanText.substring(2, 13).split("") : cleanText.split("");

    let formatted = `+55(${numbers.slice(0, 2).join("")})`;

    if (numbers.length > 2)
        formatted += ` ${numbers.slice(2, 7).join("")}`;

    if (numbers.length > 7)
        formatted += `-${numbers.slice(7, 13).join("")}`;

    return formatted;
}

function replaceCharacter(text, regex) {
    return text.replace(regex, "");
}

function maximumCharacters(text, size) {
    return (text.length > size) ? text.slice(0, size) : text;
}
