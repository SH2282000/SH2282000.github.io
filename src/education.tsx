import React from 'react';
import { useTranslation } from 'react-i18next';

const Education: React.FC = () => {
    const { t } = useTranslation();

    const educationItems = t('education', { returnObjects: true }) as {
        institution: string;
        location: string;
        degree?: string;
        date: string;
        image: string;
        skills: string[];
    }[];


    return (
        <>
            <h2>{t('sections.professionalSummary')}</h2>


            <section className="resume">
                {educationItems.map((item, index) => (
                    <div className="event" key={index}>
                        <div className="graphic">
                            <h3>{item.date}</h3>

                            {item.image && (
                                <div className="boxImg">
                                    <img src={item.image} alt={item.degree || `education-${index}`} />
                                </div>
                            )}
                        </div>

                        <div className="details">
                            {item.degree && <h4 className="font-semibold text-lg">{item.degree}</h4>}
                            {item.location && <p className="text-sm text-gray-500 italic">{item.location}</p>}

                            {item.skills && item.skills.length > 0 && (
                                <div className="flex flex-wrap gap-2 mt-3">
                                    {item.skills.map((skill, i) => (
                                        <span
                                            key={i}
                                            className="px-2 py-1 bg-gray-100 text-gray-700 text-sm rounded-full border hover:bg-gray-200 transition"
                                        >
                                            {skill}
                                        </span>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                ))}
            </section>
        </>
    );
};

export default Education;