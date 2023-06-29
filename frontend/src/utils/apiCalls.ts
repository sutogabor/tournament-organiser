export async function apiGet (URL:string) {
    const response :Response = await fetch(URL);
    return response.json();
}

export async function apiPost (payload:any, URL:string, message:string)  {
    try {
        const response: Response = await fetch(URL, {
            method: 'POST',
            headers: {
                'content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        if (response.ok) {
            alert(message);
        } else {
            alert('OOPS! Something went wrong.')
        }
    } catch (error) {
        console.log(error);
    }
}