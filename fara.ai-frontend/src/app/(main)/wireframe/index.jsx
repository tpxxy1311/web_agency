import React from 'react';
import MainHeader from '../../../components/MainHeader';
import Section from '../../../components/Section';

const WireframePage = () => {
    return (
        <main> {/* Use semantic main element */}
            <MainHeader title="Welcome to Our Site" />

            <Section title="Cookies" content="Paragraph under 'Cookies'" />
            <Section title="Use of Data" content="Paragraph explaining the use of data." />
            <Section title="Legal Information" content="Relevant legal information details." />

        </main>
    );
};

export default WireframePage;