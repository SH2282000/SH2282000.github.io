import React from 'react';
import { useTranslation } from 'react-i18next';

const Resume: React.FC = () => {
    const { t } = useTranslation();

    const resumeItems = t('resume.items', { returnObjects: true }) as {
        description: string;
        skills: string[];
        company?: string;
        location?: string;
        date: string;
        image?: string;
        text: string;
    }[];

    return (
        <>
            <h2>{t('sections.professionalSummary')}</h2>

            <section className="resume">
                {resumeItems.map((item, index) => (
                    <div className="event" key={index}>
                        <div className="graphic">
                            <h3>{item.date}</h3>

                            {item.image && (
                                <div className="boxImg">
                                    <img src={item.image} alt={item.company || `event-${index}`} />
                                </div>
                            )}
                        </div>

                        <div className="details">
                            {item.company && <h4 className="font-semibold text-lg">{item.company}</h4>}
                            {item.location && <p className="text-sm text-gray-500 italic">{item.location}</p>}

                            <p className="mt-2">{item.description}</p>

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

export default Resume;