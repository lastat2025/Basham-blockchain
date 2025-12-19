import type { MetaFunction } from "@remix-run/node";

export const meta: MetaFunction = () => {
  return [
    { title: "Basham Blockchain" },
    {
      name: "description",
      content: "A simple blockchain implementation with Vercel Analytics",
    },
  ];
};

export default function Index() {
  return (
    <div style={{ fontFamily: "system-ui, sans-serif", lineHeight: "1.8" }}>
      <h1>Welcome to Basham Blockchain</h1>
      <p>
        This is a Remix application with Vercel Web Analytics integrated.
      </p>
      <p>
        Analytics data is automatically collected and sent to Vercel for
        tracking your application&apos;s performance.
      </p>
      <ul>
        <li>Lightning fast by default</li>
        <li>Designed for all JavaScript runtimes</li>
        <li>Blockchain-powered transactions</li>
      </ul>
    </div>
  );
}
