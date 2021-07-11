import { csrf_token } from '../vars'
import Cookies from "js-cookie";

export default function (url, options, seconds = 60 * 3) {
    csrf_token = Cookies.get('csrftoken');

    return Promise.race([
        fetch(url, options),
        new Promise((_, reject) =>
            setTimeout(() => reject(new Error('timeout')), seconds * 1000)
        )
    ]);
}
