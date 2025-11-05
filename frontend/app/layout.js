import './globals.css'

export const metadata = {
  title: 'Neurobud - Mental Wellness Companion',
  description: 'A safe space to process your feelings',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}