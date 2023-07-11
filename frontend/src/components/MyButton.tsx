
const MyButton = ({className, text}: {text: string, className:string}) => {
    return(
        <div>
            <button className={className}>
                {text}
            </button>
        </div>
    )
}

export default MyButton