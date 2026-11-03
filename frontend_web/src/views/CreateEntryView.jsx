import React from 'react';
import { GratitudeForm } from '../components/GratitudeForm';

export const CreateEntryView = () => {
  return (
    <div>
      <GratitudeForm isEditing={false} />
    </div>
  );
};
