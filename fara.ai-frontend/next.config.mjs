/** @type {import('next').NextConfig} */
const nextConfig = {
    sassOptions: {
        prependData: `@use "../global/styleguide.scss";`,
      },
};

export default nextConfig;
