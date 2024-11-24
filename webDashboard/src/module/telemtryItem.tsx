type Props = {
  className: string;
  title: string;
  children?: React.ReactNode;
};

function TelemetryContainer({ className, title, children }: Props) {
  return (
    <div className={`flex flex-col justify-center items-center ${className}`}>
      <div className="flex self-stretch">
        <div className="mt-3 h-4 w-full border-l-2 border-t-2 rounded-tl-xl" />
        <span className="text-xl mb-3.5 px-1 text-nowrap">{title}</span>
        <div className="mt-3 h-4 w-full border-r-2 border-t-2 rounded-tr-xl" />
      </div>

      <div className="pb-2 relative flex h-full align-middle justify-center border-x-2 border-b-2 rounded-b-xl -mt-3.5">
        <div className="absolute inset-0 mx-5 mb-5 blur-xl bg-gray-700"></div>
        <div className="relative flex items-center justify-center">{children}</div>
      </div>
    </div>
  );
}

export default TelemetryContainer;
