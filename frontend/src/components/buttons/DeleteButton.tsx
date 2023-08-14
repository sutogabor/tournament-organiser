import React, { useState } from 'react';

interface DeleteButtonProps {
    onDelete: () => void;
    isLoading: boolean;
}

const DeleteButton: React.FC<DeleteButtonProps> = ({ onDelete, isLoading }) => {

    const [isConfirmVisible, setIsConfirmVisible] = useState(false);

    const handleDeleteClick = () => {
        if (isLoading) {
            return;
        }

        if (isConfirmVisible) {
            onDelete();
            setIsConfirmVisible(false);
        } else {
            setIsConfirmVisible(true);
        }
    };

    return (
        <div className="card-delete-button">
            {isConfirmVisible ? (
                <>
                    <p>Are you sure?</p>
                    <button onClick={handleDeleteClick}>Yes</button>
                    <button onClick={() => setIsConfirmVisible(false)}>No</button>
                </>
            ) : (
                <button onClick={handleDeleteClick}>
                    {isLoading ? 'Deleting...' : 'Delete'}
                </button>
            )}
        </div>
    );
};

export default DeleteButton;
