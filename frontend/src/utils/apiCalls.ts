export async function apiGet(URL: string) {
    try {
        const response: Response = await fetch(URL, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });
        if (response.ok) {
            return await response.json();
        } else {
            throw new Error("Bad response at apiCalls.apiGet()");
        }
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function apiPost(payload: any, URL: string, message: string) {
    try {
        const response: Response = await fetch(URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (response.ok) {
            alert(message);
        } else {
            alert('Bad response at apiCalls.apiPost()')
        }
    } catch (error) {
        console.log(error);
    }
}