export default function (url, options, seconds = 60 * 3) {
    return Promise.race([
        fetch(url, options),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('timeout')), seconds * 1000)
        )
    ]);
}
